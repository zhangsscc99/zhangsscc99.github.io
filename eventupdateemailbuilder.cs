using System.IO;
using MimeKit;
using Microsoft.AspNetCore.Identity.UI.Services;
using GamePlay.Data;
using System;

namespace GamePlay.Services.EmailBuilderService
{
    public class EventUpdateEmailBuilder : IEmailBuilder_Interface
    {
        public EventUpdateEmailBuilder(string subject, string webRootPath, string templateFile, 
                                        EventFC eventFC, string buttonName, string buttonUrl, 
                                        EventFC oldEvent, string receiverName, string senderName,
                                        string team)
        {
            Subject = subject;

            //Get TemplateFile located at wwwroot/Templates/EmailTemplate/{templateFile}  
            TemplatePath = webRootPath
                            + Path.DirectorySeparatorChar.ToString()
                            + "Templates"
                            + Path.DirectorySeparatorChar.ToString()
                            + "EmailTemplate"
                            + Path.DirectorySeparatorChar.ToString()
                            + templateFile;
            EventFC = eventFC;
            OldEvent = oldEvent;
            ButtonName = buttonName;
            ButtonUrl = buttonUrl;
            ReceiverName = receiverName;
            SenderName = senderName;
            Team = team;
            //ResponseName = responseName;
        }

        public string Subject { get; set; }
        public string TemplatePath { get; set; }

        public string ButtonName { get; set; }
        public string ButtonUrl { get; set; }
        public EventFC EventFC { get; set; }
        public EventFC OldEvent { get; set; }
        public string ReceiverName { get; set; }
        public string  SenderName { get; set; }
        public string Team { get; set; }

        //public string ResponseName { get; set; }

        /// <summary>
        /// Construct the email's body with the email template file and values
        /// </summary>
        /// <returns></returns>
        public string CustomizeTemplate()
        {   
            string[] eventTypeName = { "Game", "Team meeting", "Practice", "Information session", "Other" };
            var builder = new BodyBuilder();
            using (StreamReader SourceReader = File.OpenText(TemplatePath))
            {
                builder.HtmlBody = SourceReader.ReadToEnd();
            }

            string messageBody = builder.HtmlBody
                .Replace("{receiverName}", ReceiverName)
                .Replace("{senderName}", SenderName)
                .Replace("{eventName}", EventFC.EventScheduleName)
                .Replace("{eventType}", eventTypeName[int.Parse(EventFC.EventTypeId) - 1])
                .Replace("{ButtonName}", ButtonName)
                .Replace("{ButtonUrl}", ButtonUrl)
                .Replace("{start}", DateTime.Parse(EventFC.StartDate).ToString())
                .Replace("{oldStart}", DateTime.Parse(OldEvent.StartDate).ToString())
                .Replace("{location}", EventFC.EventLocation)
                .Replace("{oldLocation}", OldEvent.EventLocation)
                .Replace("{teamName}", Team);
                //.Replace("{responseName}", ResponseName);

            return messageBody;
        }

        /// <summary>
        /// Send the email to user's email address
        /// </summary>
        /// <param name="_emailSender"></param>
        /// <param name="Email"></param>
        /// <param name="messageBody"></param>
        public async void SendEmail(IEmailSender _emailSender, string Email, string messageBody)
        {
            await _emailSender.SendEmailAsync(Email, Subject, messageBody);
        }
    }
}