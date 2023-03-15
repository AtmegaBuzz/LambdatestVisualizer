import "./App.css";
import { createContext, useState, useEffect } from "react";
import {Route,Routes} from "react-router-dom";
import Home from "./pages/Home";
import Mime from "./pages/Mime";
import Status from "./pages/Status";
import Navbar from "./components/Navbar";

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


  return (
    <LogsContext.Provider value={contextData}>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Home/>}/>
          <Route path="/status-logs" element={<Status/>}/>
          <Route path="/mime-logs" element={<Mime/>}/>
        </Routes>
    </LogsContext.Provider>
  );
}

export default App;
