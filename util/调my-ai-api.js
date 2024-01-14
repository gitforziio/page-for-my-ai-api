import axios from 'axios';

const backendUrl = "";
const password = "";

const useAI = async (
  query, task, reqFormat, resFormat,
  model="gpt-3.5-turbo-1106",
) => {
  try {
    if (!query?.length) throw new Error("query is empty");
    if (!task?.length) throw new Error("task is empty");
    const res = await axios.post(backendUrl, {
      query,
      task,
      reqFormat,
      resFormat,
      model,
      password,
    });
    return res.data;
  } catch (err) {
    console.error(err);
    return {type: "error", error: err};
  }
};

const useAI4 = async (query, task, reqFormat, resFormat) => {
  return await useAI(query, task, reqFormat, resFormat, "gpt-4-1106-preview");
}

