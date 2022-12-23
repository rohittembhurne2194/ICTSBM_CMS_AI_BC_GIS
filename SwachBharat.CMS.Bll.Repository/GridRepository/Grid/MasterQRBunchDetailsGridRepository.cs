using SwachBharat.CMS.Bll.ViewModels.ChildModel.Grid;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SwachBharat.CMS.Bll.Repository.GridRepository.Grid
{
    public class MasterQRBunchDetailsGridRepository : IDataTableRepository
    {
        IEnumerable<SBAHouseDetailsGridRow> dataSet;
        DashBoardRepository objRep = new DashBoardRepository();

        public MasterQRBunchDetailsGridRepository(long wildcard, string SearchString,string IsActive, int appId)
        {
            dataSet = objRep.GetMasterQRBunchDetailsData(wildcard, SearchString, IsActive, appId);
        }

        public string GetDataTabelJson(string sortColumn, string sortColumnDir, string draw, string length, string searchValue, string start)
        {
            var json = dataSet.GetDataTableJson(sortColumn, sortColumnDir, draw, length, searchValue, start);
            return json;
        }
    }

}
