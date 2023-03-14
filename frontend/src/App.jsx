import "./App.css";
import { createContext, useState, useEffect } from "react";
import TotalLogs from "./components/Logs";
import MimeLogs from "./components/mimeType";
import StatusCodeLogs from "./components/statusCode";

export const LogsContext = createContext();

function App() {
  const [yearLogCount, setYearLogCount] = useState([]);

  const [mimeTypes, setMimeTypes] = useState([]);
  const [yearMimeTypeLogs, setYearMimeTypeLogs] = useState([]);
  const [mimePieData, setMimePieData] = useState([]);
  const [filterMimeType, setFilterMimeType] = useState([]);

  const [statusCodes, setStatusCodes] = useState([]);
  const [yearStatusCodeLogs, setYearStatusCodeLogs] = useState([]);
  const [statusPieData, setStatusPieData] = useState([]);
  const [filterStatusCode, setfilterStatusCode] = useState([]);

  const contextData = {
    yearLogCount,
    mimeTypes,
    yearMimeTypeLogs,
    mimePieData,
    filterMimeType,
    statusCodes,
    yearStatusCodeLogs,
    statusPieData,
    filterStatusCode,

    setYearLogCount,
    setMimeTypes,
    setYearMimeTypeLogs,
    setMimePieData,
    setFilterMimeType,
    setStatusCodes,
    setYearStatusCodeLogs,
    setStatusPieData,
    setfilterStatusCode,
  };

  const get_log_count = async () => {
    let resp = await fetch("http://127.0.0.1:8000");
    let data = await resp.json();
    setYearLogCount(data);
  };

  //  Mime types logs API calls
  const get_mimeTypes = async () => {
    let resp = await fetch("http://127.0.0.1:8000/mimeType");
    let data = await resp.json();
    setMimeTypes(data);
  };

  const get_year_mimetype_logs = async () => {
    let resp = await fetch("http://127.0.0.1:8000/mimeType", {
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({
        mimeType: filterMimeType,
      }),
    });
    let data = await resp.json();
    setYearMimeTypeLogs(data["count"]);
  };

  const get_mime_pie_data = async () => {
    let resp = await fetch("http://127.0.0.1:8000/mimeTypesLog");
    let data = await resp.json();
    setMimePieData(data);
  };
  // Mime type API call ENDS

  //  Status code logs API calls
  const get_statusCodes = async () => {
    let resp = await fetch("http://127.0.0.1:8000/statusCode");
    let data = await resp.json();
    setStatusCodes(data);
  };

  const get_year_statuscode_logs = async () => {
    let resp = await fetch("http://127.0.0.1:8000/statusCode", {
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({
        statusCode: filterStatusCode,
      }),
    });
    let data = await resp.json();
    setYearStatusCodeLogs(data["count"]);
  };

  const get_status_pie_data = async () => {
    let resp = await fetch("http://127.0.0.1:8000/statusCodeLogs");
    let data = await resp.json();
    setStatusPieData(data);
  };
  // Status code API call ENDS

  useEffect(() => {
    get_log_count();

    get_mimeTypes();
    get_mime_pie_data();
    
    get_statusCodes();
    get_status_pie_data()
  }, []);

  useEffect(() => {
    get_year_mimetype_logs();
  }, [filterMimeType]);

  useEffect(()=>{
    get_year_statuscode_logs();
  },[filterStatusCode])

  return (
    <LogsContext.Provider value={contextData}>
      <div className="App">
        <TotalLogs />
        <MimeLogs />
        <StatusCodeLogs/>
      </div>
    </LogsContext.Provider>
  );
}

export default App;
