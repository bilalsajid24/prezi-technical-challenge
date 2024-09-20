import { PresentationsResponse } from "./types/presentations";

export const fetcher = async (url: string): Promise<PresentationsResponse> => {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || "";
  const fullUrl = url.startsWith(apiUrl) ? url : `${apiUrl}${url}`;

  const response = await fetch(fullUrl);
  if (!response.ok) {
    throw new Error("Failed to fetch");
  }
  return response.json();
};
