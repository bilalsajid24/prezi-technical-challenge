import useSWR from "swr";

import { fetcher } from "@/api";
import { PresentationsResponse } from "@/types/presentations";

const usePresentations = (search: string, ordering: string, pageUrl: string | null) => {
  let baseUrl = `/api/v1/presentations?ordering=${ordering}`;

  if (search) {
    baseUrl = `${baseUrl}&search=${search}`;
  }
  const url = pageUrl || baseUrl;

  const { data, error, isValidating } = useSWR<PresentationsResponse>(url, fetcher, { revalidateIfStale: false, revalidateOnFocus: false, revalidateOnReconnect: false });

  return {
    presentations: data?.results || [],
    error,
    isValidating,
    nextPage: data?.next,
    prevPage: data?.previous,
  };
};

export default usePresentations;
