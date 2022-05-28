import axios from "axios";

const baseURL = "http://localhost:8000/";

export const HTTP = axios.create({
    baseURL: baseURL,
    headers: {
        "Content-Type": "application/json",
    }
});
