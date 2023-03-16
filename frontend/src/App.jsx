import "./App.css";
import { createContext, useState, useEffect } from "react";
import {Route,Routes} from "react-router-dom";
import Home from "./pages/Home";
import Mime from "./pages/Mime";
import Status from "./pages/Status";
import Navbar from "./components/Navbar";
import Logs from "./pages/Logs";
import LogDetail from "./pages/LogDetail";

export const LogsContext = createContext();

function App() {

  // home page state
  const [yearLogCount, setYearLogCount] = useState([]);

  // mime page state
  const [mimeTypes, setMimeTypes] = useState([]);
  const [yearMimeTypeLogs, setYearMimeTypeLogs] = useState([]);
  const [mimePieData, setMimePieData] = useState([]);
  const [filterMimeType, setFilterMimeType] = useState([]);

  // status code state
  const [statusCodes, setStatusCodes] = useState([]);
  const [yearStatusCodeLogs, setYearStatusCodeLogs] = useState([]);
  const [statusPieData, setStatusPieData] = useState([]);
  const [filterStatusCode, setfilterStatusCode] = useState([]);
  
  // logs page state
  const [networkLogs,setNetworkLogs] = useState([]);
  
  // nav filter state 
  const [filterKey,setFilterKey] = useState("");
  const [filterValue,setFilterValue] = useState("");

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
    networkLogs,
    filterKey,
    filterValue,



    setYearLogCount,
    setMimeTypes,
    setYearMimeTypeLogs,
    setMimePieData,
    setFilterMimeType,
    setStatusCodes,
    setYearStatusCodeLogs,
    setStatusPieData,
    setfilterStatusCode,
    setNetworkLogs,
    setFilterKey,
    setFilterValue
  };


  return (
    <LogsContext.Provider value={contextData}>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/status-logs" element={<Status/>}/>
          <Route path="/mime-logs" element={<Mime/>}/>
          <Route path="/logs" element={<Logs/>}/>
          <Route path="/log" element={<LogDetail/>}/>
        </Routes>
    </LogsContext.Provider>
  );
}

export default App;
