// Written by Akul Mehra

using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using GamePlay.Dal.Model;
using GamePlay.Data;
using GamePlay.Services;
using GamePlay.ViewModel;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.UI.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Caching.Memory;
using Microsoft.AspNetCore.Http;
using Microsoft.CodeAnalysis;
using GoogleApi.Entities.Search.Video.Common;
using GamePlay.Services.EmailBuilderService;
using System.Text.RegularExpressions;
using System.Text.Encodings.Web;


namespace GamePlay.Controllers
{
    [Authorize]
    [Route("api/[controller]")]
    [ApiController]
    public class BookFieldAPIController : GPBaseController
    {
        private readonly GamePlayContext _context;
        private readonly IFieldRepository _fieldRepo;
        private readonly IEmailSender _emailSender;
        private IWebHostEnvironment _env;

        public BookFieldAPIController(RoleManager<ApplicationRole> roleManager, UserManager<ApplicationUser> userManager, 
            IEmailSender emailSender, GamePlayContext context, IConfiguration config, ICookieManager cookieManager, 
            IWebHostEnvironment env, IFieldRepository fieldRepo, IMemoryCache memoryCache)
            : base(roleManager, userManager, emailSender, context, config, cookieManager, memoryCache)
        {
            _context = context;
            _fieldRepo = fieldRepo;
            _emailSender = emailSender;
            _env = env;
        }

        // Method to get the availability of a single day of a particular field
        // Params:-
        // string id: FieldId of the field selected by the user
        // DateTime startDate: The start date of the booking selected by the user
        // DateTime endDate: The end date of the booking selected by the user
        [HttpGet("{id}")]
        public async Task<ActionResult<BookFieldViewModel>> GetAvailability(string id, DateTime startDate, DateTime endDate) {
            if (id == null) {
                return null;
            }
            if (startDate == null) {
                return null;
            }

            // Getting basic information based on field id
            int fieldId = int.Parse(id);

            // Checking if field of given fieldId is available (basic null check)
            if (!_fieldRepo.isFieldAvailable(fieldId)) {
                return new BookFieldViewModel();
            }

            // Getting prices
            decimal? unitPrice = await _fieldRepo.GetUnitPrice(fieldId);
            decimal? lightsPrice;
            string lightsStatus =  _fieldRepo.GetLightsStatus(fieldId);
            if (lightsStatus.ToLower() == "yes")
            {
                lightsPrice = _fieldRepo.GetLightsPrice(fieldId);

            }
            else {
                lightsPrice = 0;
            }

            //Getting general booking date
            string generalBookingDate = _fieldRepo.GetGeneralDateStr(fieldId);


            decimal? misusePenaltyPrice = _fieldRepo.GetMisusePenaltyPrice(fieldId);

            // Initializing and assigning values to the view model to be returned
            BookFieldViewModel fieldAvailability = new BookFieldViewModel();

            fieldAvailability.AvailableTimeSlots = await _fieldRepo.GetTimeSlots(fieldId, startDate, endDate);

            var currentUser = await UserManager.GetUserAsync(User);
            var ContactId = (await GamePlayDbContext.Contact.FirstAsync(c => c.MembershipId == currentUser.Id)).ContactId;
            if (generalBookingDate!= null){
                fieldAvailability.PriorityCheck = _fieldRepo.CheckPriority(ContactId, fieldId, startDate);
            }
            fieldAvailability.GeneralBookingDate = generalBookingDate;

            fieldAvailability.FieldId = id;
            fieldAvailability.UnitPrice = unitPrice;
            fieldAvailability.Date = startDate;
            fieldAvailability.LightPrice = lightsPrice;
            fieldAvailability.LightsStatus = lightsStatus;
            fieldAvailability.MisusePrice = misusePenaltyPrice;
            fieldAvailability.MinBookingHours =  _fieldRepo.GetMinimumBookingTime(fieldId);
            fieldAvailability.FieldAvailabilityId = _fieldRepo.GetAvailabilityId(fieldId, startDate).ToString();
            fieldAvailability.Selected = false;

            return fieldAvailability;
        }


        


        [HttpPost("SignUp")]
        public async Task<Boolean> SignUp(BookedFields b)
        {
            try
            {
                System.Diagnostics.Debug.WriteLine("herererererere");
                //int booking_id = (int)b.field_booking_id;
                int event_schedule_id = (int)b.event_schedule_id;
                //System.Diagnostics.Debug.WriteLine("id is: "+booking_id);
                System.Diagnostics.Debug.WriteLine("test_schedule is: " + event_schedule_id);

                EventSchedule es = await GamePlayDbContext.EventSchedule
                    .Include(e => e.EventMember)
                    .FirstAsync(e => e.EventScheduleId == event_schedule_id);



                var user = await base.getCurrentUserMain();


                var eventSchedule = await GamePlayDbContext.EventSchedule
                    .Include(es => es.Contact) // ensure that we have contact
                    .FirstAsync(e => e.EventScheduleId == event_schedule_id);

                
                var creatorEmail = eventSchedule.Contact?.EmailAddress;
                var creatorFirstName = eventSchedule.Contact?.FirstName;
                var eventLocation = eventSchedule.EventLocation;
                eventLocation = Regex.Replace(eventLocation, @"\p{IsCJKUnifiedIdeographs}", string.Empty);
                var eventStart = eventSchedule.StartDate;
                var eventName = eventSchedule.EventScheduleName;
                string eventStartString = "" + eventStart;

               

                var subject = "Signup for the Event";
                string webRootPath = _env.WebRootPath;
                string templateFile = "GameResponse_EmailTemplate.html";
                EventFC eventDetails = new EventFC();
                EventFC oldEvent = new EventFC();
                EventFC oldEventDetails = new EventFC();
                string buttonName = "View Event";
                string buttonUrl = HtmlEncoder.Default.Encode("www.google.com");

                string receiverName = creatorFirstName;
                string senderName = user.FirstName;
                string team = "Default Team";
                string responseName = user.FirstName;

                


                GameResponseEmailBuilder emailBuilder = new GameResponseEmailBuilder(subject, webRootPath, templateFile,
                    //eventDetails, buttonName, buttonUrl, oldEventDetails, 
                    eventName, eventStartString, eventLocation,  
                    receiverName, senderName, team, responseName, buttonName);


                string messageBody = emailBuilder.CustomizeTemplate();
                emailBuilder.SendEmail(_emailSender, creatorEmail, messageBody);






               


                if (GamePlayDbContext.EventMember.Where(e => e.EventScheduleId == es.EventScheduleId).Where(e => e.ContactId == user.ContactId).Count() == 0)
                {
                    EventMember em = new EventMember();
                    em.EventScheduleId = es.EventScheduleId;
                    em.ContactId = user.ContactId;
                    em.MemberType = "game_response";
                    em.Status = "Pending";
                    GamePlayDbContext.EventMember.Add(em);
                    
                    ViewBag.msg = "Sign Up Successfully!";
                }
                else if(GamePlayDbContext.EventMember.Where(e => e.EventScheduleId == es.EventScheduleId).Where(e => e.ContactId == user.ContactId).Count() != 0)
                {
                    EventMember em = await GamePlayDbContext.EventMember.Where(e => e.EventScheduleId == event_schedule_id).FirstAsync(e => e.ContactId == user.ContactId);
                    em.Status = "Pending";
                    
                }
                else
                {
                    ViewBag.msg = "You have already signed up for this game!";
                }

                //var bookedField = await GamePlayDbContext.FieldBooking
                //    .Include(fb => fb.FieldAvailability)
                //    .ThenInclude(fa => fa.Field)
                //        .ThenInclude(f => f.Facility)
                //            .ThenInclude(fac => fac.Address).FirstOrDefaultAsync(f => f.FieldBookingId == booking_id);

                await GamePlayDbContext.SaveChangesAsync();
                return true;
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine("error: "+ex);
                return false;
            }
            //return View(bookedField);
        }

        [HttpPost("RemoveSignUp")]
        public async Task<Boolean> RemoveSignUp(BookedFields b)
        {
            try
            {
                int event_schedule_id = (int)b.event_schedule_id;
                System.Diagnostics.Debug.WriteLine("test_schedule for remove is: " + event_schedule_id);

                EventSchedule es = await GamePlayDbContext.EventSchedule
                    .Include(e => e.EventMember)
                    .FirstAsync(e => e.EventScheduleId == event_schedule_id);
                var user = await base.getCurrentUserMain();
                EventMember em = await GamePlayDbContext.EventMember.Where(e => e.EventScheduleId == event_schedule_id).FirstAsync(e => e.ContactId == user.ContactId);
                em.Status = "deleted";

                await GamePlayDbContext.SaveChangesAsync();
                return true;
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine("error: " + ex);
                return false;
            }
            //return View(bookedField);
        }



        [HttpPost("ChangeEventSchedule")]
        public async Task<Boolean> ChangeEventSchedule(BookedFields b)
        {
            try
            {
                //int booking_id = (int)b.field_booking_id;

                System.Diagnostics.Debug.WriteLine("event creater is: " + b.event_owner_contactID);
                
                var user = await base.getCurrentUserMain();
                System.Diagnostics.Debug.WriteLine("current user is: " + user.ContactId);
                if (user.ContactId == b.event_owner_contactID)
                {
                    string fieldName = b.field_name;
                    //System.Diagnostics.Debug.WriteLine("start time is: " + b.s_time);
                    //System.Diagnostics.Debug.WriteLine("end time is: " + b.e_time);
                    //System.Diagnostics.Debug.WriteLine("start date is: " + b.s_date);
                    //System.Diagnostics.Debug.WriteLine("end date is: " + b.e_date);
                    //System.Diagnostics.Debug.WriteLine("startDate is: " + b.start_date);

                    EventSchedule es = await GamePlayDbContext.EventSchedule
                        //.Include(e => e.EventMember)
                        .FirstAsync(e => e.EventScheduleId == b.event_schedule_id);
                    string start_date_time = b.s_date + " " + b.s_time + ":00";
                    string end_date_time = b.e_date + " " + b.e_time + ":00";
                    System.Diagnostics.Debug.WriteLine("start_date_time is: " + start_date_time);
                    System.Diagnostics.Debug.WriteLine("end_date_time is: " + end_date_time);
                    es.StartDate = DateTime.Parse(start_date_time);
                    es.EndDate = DateTime.Parse(end_date_time);
                    es.FieldId = b.field_id;
                    await GamePlayDbContext.SaveChangesAsync();
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine("error: " + ex);
                return false;
            }
            //return View(bookedField);
        }
    }
}
