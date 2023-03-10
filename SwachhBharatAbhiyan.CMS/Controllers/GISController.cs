using SwachhBharatAbhiyan.CMS.Models.SessionHelper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace SwachhBharatAbhiyan.CMS.Controllers
{
    public class GISController : Controller
    {
        // GET: GIS
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult GisMap()
        {
            //string appid = SessionHandler.Current.AppId.ToString();
            //string token = SessionHandler.Current.Token.ToString();
       

            ViewBag.Username = SessionHandler.Current.GisUsername;
            ViewBag.Password = SessionHandler.Current.GisPassword;

            //ViewBag.myURL = "http://114.143.244.130:8080?appid=" + appid + "&token=" + token; // set your dynamic URL here

            ViewBag.myURL = "http://114.143.244.130:8080?";
            return View();
        }
    }
}