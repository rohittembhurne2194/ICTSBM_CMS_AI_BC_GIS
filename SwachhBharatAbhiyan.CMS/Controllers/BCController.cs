using SwachBharat.CMS.Bll.Repository.ChildRepository;
using SwachBharat.CMS.Bll.Repository.MainRepository;
using SwachhBharatAbhiyan.CMS.Models.SessionHelper;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace SwachhBharatAbhiyan.CMS.Controllers
{
    public class BCController : Controller
    {

        IMainRepository mainRepository;
        IChildRepository childRepository;


        public BCController()
        {
            if (SessionHandler.Current.AppId != 0)
            {
                mainRepository = new MainRepository();
                childRepository = new ChildRepository(SessionHandler.Current.AppId);
            }
            else
                Redirect("/Account/Login");
        }
        public ActionResult MenuBCDumpYardIndex()
        {
            if (SessionHandler.Current.AppId != 0)
            {
                return View();
            }
            else
                return Redirect("/Account/Login");
        }


        public ActionResult BCDumpYardIndex()
        {
            if (SessionHandler.Current.AppId != 0)
            {
             //   var details = childRepository.GetDashBoardDetails();
                return View();
            }
            else
                return Redirect("/Account/Login");
        }
    }
}