using SwachhBharatAbhiyan.CMS.Models.SessionHelper;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.Mvc;

namespace SwachhBharatAbhiyan.CMS.Controllers
{
    public class AIReportsController : Controller
    {
        // GET: AIReports
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult DumpYardForecastReport()
        {


            //var test = Process.Start("D:/Rohit/AI_Documents/heatmap_Armori.py");
            //return View(test);
            var IP = SessionHandler.Current.DB_Source;
            var DB = SessionHandler.Current.DB_Name;
            var ULB_Name = SessionHandler.Current.AppName;

            string trim_ULB_Name = ULB_Name.Replace(" ", "");

            var psi = new ProcessStartInfo();
            string HostName = Request.Url.Host;
            string port = Convert.ToString(Request.Url.Port);

            Console.WriteLine("The Hostname are = " + HostName);
            string path = Server.MapPath("~/Images/AI/" + trim_ULB_Name + "/DumpYardforecast.html");
            FileInfo file = new FileInfo(path);
            if (file.Exists)
            {
                file.Delete();
                Console.WriteLine("File deleted.");
            }
            if (HostName == "localhost")
            {
                psi.FileName = @"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment


            }
            else
            {
                HostName = HostName + ":" + port;
                psi.FileName = @"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment

               

            }

            //psi.Arguments = $"\"D:/Rohit/ICTSBM_CMS_AI_TEST_NEW/SwachhBharatAbhiyan.CMS/AI_ReportsFiles/EmpWise_Collection.py";
            // string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/EmpWise_Collection.py");
            string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/DumpYardForeCast/forecast_deply_1.py");

            psi.Arguments = string.Format("{0} {1} {2} {3} {4} {5} {6}", pythonfile, "-ip " + IP, "-db " + DB, "-ulbname " + trim_ULB_Name, "-hostname " + HostName, "-filename DumpYardForecast", "-ReportTitle " + '"' + ULB_Name + '"');


            psi.UseShellExecute = false;
            psi.CreateNoWindow = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.StandardOutputEncoding = Encoding.UTF8;

            string errors = "", result = "";

            using (var process = Process.Start(psi))
            {
                result = process.StandardOutput.ReadToEnd();
                errors = process.StandardError.ReadToEnd();

            }
            StringWriter writer = new StringWriter();
            HttpUtility.HtmlDecode(result, writer);
            var decodedString = writer.ToString();

            ViewBag.AIReportFolder = trim_ULB_Name;
            return View();
        }

        public ActionResult DumpYardForecastBarReport()
        {


            //var test = Process.Start("D:/Rohit/AI_Documents/heatmap_Armori.py");
            //return View(test);
            var IP = SessionHandler.Current.DB_Source;
            var DB = SessionHandler.Current.DB_Name;
            var ULB_Name = SessionHandler.Current.AppName;

            string trim_ULB_Name = ULB_Name.Replace(" ", "");

            var psi = new ProcessStartInfo();
            string HostName = Request.Url.Host;
            string port = Convert.ToString(Request.Url.Port);


            string path = Server.MapPath("~/Images/AI/" + trim_ULB_Name + "/DumpYardforecastbar.html");
            FileInfo file = new FileInfo(path);
            if (file.Exists)
            {
                file.Delete();
                Console.WriteLine("File deleted.");
            }
            if (HostName == "localhost")
            {
                psi.FileName = @"C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment


            }
            else
            {
                HostName = HostName + ":" + port;
                psi.FileName = @"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment

            }

            //psi.Arguments = $"\"D:/Rohit/ICTSBM_CMS_AI_TEST_NEW/SwachhBharatAbhiyan.CMS/AI_ReportsFiles/EmpWise_Collection.py";
            // string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/EmpWise_Collection.py");
            string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/DumpYardForeCast/forecast_gg_bar_deply.py");

            psi.Arguments = string.Format("{0} {1} {2} {3} {4} {5} {6}", pythonfile, "-ip " + IP, "-db " + DB, "-ulbname " + trim_ULB_Name, "-hostname " + HostName, "-filename DumpYardForecastbar", "-ReportTitle " + '"' + ULB_Name + '"');


            psi.UseShellExecute = false;
            psi.CreateNoWindow = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.StandardOutputEncoding = Encoding.UTF8;

            string errors = "", result = "";

            using (var process = Process.Start(psi))
            {
                result = process.StandardOutput.ReadToEnd();
                errors = process.StandardError.ReadToEnd();

            }
            StringWriter writer = new StringWriter();
            HttpUtility.HtmlDecode(result, writer);
            var decodedString = writer.ToString();

            ViewBag.AIReportFolder = trim_ULB_Name;
            return View();
        }

        public ActionResult HouseCountForecastReport()
        {

            //var test = Process.Start("D:/Rohit/AI_Documents/heatmap_Armori.py");
            //return View(test);
            var IP = SessionHandler.Current.DB_Source;
            var DB = SessionHandler.Current.DB_Name;
            var ULB_Name = SessionHandler.Current.AppName;

            string trim_ULB_Name = ULB_Name.Replace(" ", "");

            var psi = new ProcessStartInfo();
            string HostName = Request.Url.Host;
            string port = Convert.ToString(Request.Url.Port);


            string path = Server.MapPath("~/Images/AI/" + trim_ULB_Name + "/HouseScanforecast.html");
            FileInfo file = new FileInfo(path);
            if (file.Exists)
            {
                file.Delete();
                Console.WriteLine("File deleted.");
            }
            if (HostName == "localhost")
            {
                psi.FileName = @"C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment


            }
            else
            {
                HostName = HostName + ":" + port;
                psi.FileName = @"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment

            }

            //psi.Arguments = $"\"D:/Rohit/ICTSBM_CMS_AI_TEST_NEW/SwachhBharatAbhiyan.CMS/AI_ReportsFiles/EmpWise_Collection.py";
            // string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/EmpWise_Collection.py");
            string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/HouseScanForecast/HouseScanForeCast.py");

            psi.Arguments = string.Format("{0} {1} {2} {3} {4} {5} {6}", pythonfile, "-ip " + IP, "-db " + DB, "-ulbname " + trim_ULB_Name, "-hostname " + HostName, "-filename HouseScanForecast", "-ReportTitle " + '"' + ULB_Name + '"');


            psi.UseShellExecute = false;
            psi.CreateNoWindow = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.StandardOutputEncoding = Encoding.UTF8;

            string errors = "", result = "";

            using (var process = Process.Start(psi))
            {
                result = process.StandardOutput.ReadToEnd();
                errors = process.StandardError.ReadToEnd();

            }
            StringWriter writer = new StringWriter();
            HttpUtility.HtmlDecode(result, writer);
            var decodedString = writer.ToString();

            ViewBag.AIReportFolder = trim_ULB_Name;
            return View();
        }

        public ActionResult HouseForecastBarReport()
        {

            //var test = Process.Start("D:/Rohit/AI_Documents/heatmap_Armori.py");
            //return View(test);
            var IP = SessionHandler.Current.DB_Source;
            var DB = SessionHandler.Current.DB_Name;
            var ULB_Name = SessionHandler.Current.AppName;

            string trim_ULB_Name = ULB_Name.Replace(" ", "");

            var psi = new ProcessStartInfo();
            string HostName = Request.Url.Host;
            string port = Convert.ToString(Request.Url.Port);


            string path = Server.MapPath("~/Images/AI/" + trim_ULB_Name + "/HouseScanforecastbar.html");
            FileInfo file = new FileInfo(path);
            if (file.Exists)
            {
                file.Delete();
                Console.WriteLine("File deleted.");
            }
            if (HostName == "localhost")
            {
                psi.FileName = @"C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment


            }
            else
            {
                HostName = HostName + ":" + port;
                psi.FileName = @"C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe"; // or any python environment

            }

            //psi.Arguments = $"\"D:/Rohit/ICTSBM_CMS_AI_TEST_NEW/SwachhBharatAbhiyan.CMS/AI_ReportsFiles/EmpWise_Collection.py";
            // string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/EmpWise_Collection.py");
            string pythonfile = System.Web.Hosting.HostingEnvironment.MapPath("~/AI_ReportsFiles/HouseScanForecast/forecast_hc_bar_deply.py");

            psi.Arguments = string.Format("{0} {1} {2} {3} {4} {5} {6}", pythonfile, "-ip " + IP, "-db " + DB, "-ulbname " + trim_ULB_Name, "-hostname " + HostName, "-filename HouseScanForecast", "-ReportTitle " + '"' + ULB_Name + '"');


            psi.UseShellExecute = false;
            psi.CreateNoWindow = false;
            psi.RedirectStandardOutput = true;
            psi.RedirectStandardError = true;
            psi.StandardOutputEncoding = Encoding.UTF8;

            string errors = "", result = "";

            using (var process = Process.Start(psi))
            {
                result = process.StandardOutput.ReadToEnd();
                errors = process.StandardError.ReadToEnd();

            }
            StringWriter writer = new StringWriter();
            HttpUtility.HtmlDecode(result, writer);
            var decodedString = writer.ToString();

            ViewBag.AIReportFolder = trim_ULB_Name;
            return View();
        }
    }
}