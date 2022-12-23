using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SwachBharat.CMS.Bll.ViewModels.Grid
{
  public  class ICTDumTripGridRow
    {


        public int TransBcId { get; set; }
        public string transId { get; set; }
        public string startDateTime { get; set; }
        public string endDateTime { get; set; }
        public string userName { get; set; }
        public string dyId { get; set; }
        public string houseList { get; set; }
        public Nullable<int> tripNo { get; set; }
        public string vehicleNumber { get; set; }
        public Nullable<decimal> totalGcWeight { get; set; }
        public Nullable<decimal> totalDryWeight { get; set; }
        public Nullable<decimal> totalWetWeight { get; set; }
        public string bcTransId { get; set; }
        public bool ? TStatus { get; set; }

        public string tHr { get; set; }
        public string tNh { get; set; }
        

    }
}
