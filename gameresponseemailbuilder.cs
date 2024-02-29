using System.IO;
using MimeKit;
using Microsoft.AspNetCore.Identity.UI.Services;


namespace GamePlay.Services.EmailBuilderService
{
    public class GameResponseEmailBuilder : IEmailBuilder_Interface
    {
        public GameResponseEmailBuilder(string subject, string webRootPath, string templateFile, string eventName, string eventStart, string eventLocation, string receiverName, string senderName,
                                        string team, string responseName, string buttonName)
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
            
            EventName = eventName;
            EventStart = eventStart;
            EventLocation = eventLocation;
            ReceiverName = receiverName;
            SenderName = senderName;
            Team = team;
            ResponseName = responseName;
            ButtonName = buttonName;
        }

        public string Subject { get; set; }
        public string TemplatePath { get; set; }

        
        public string ReceiverName { get; set; }
        public string  SenderName { get; set; }
        public string Team { get; set; }

        public string ResponseName { get; set; }

        public string EventName { get; set; }

        public string EventStart { get; set; }

        public string EventLocation { get; set; }

        public string ButtonName { get; set; }

        

        

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
                .Replace("{teamName}", Team)
                .Replace("{responseName}", ResponseName)
                .Replace("{eventName}", EventName)
                .Replace("{start}", EventStart)
                .Replace("{location}", EventLocation)
                .Replace("{ButtonName}", ButtonName);

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