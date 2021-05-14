import axios from "axios";
// 初始化一个 axios 类, 可以发送 http 请求
const instance = axios.create({
  // 服务的基地址
  baseURL: "http://localhost:5000",
  // 超时时间
  timeout: 1000,
});

// 导出 instance , 只有导入后, 其它文件才能使用 instance
export default instance;
