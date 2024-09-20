export interface Creator {
  id: string;
  name: string;
  profile_url: string;
}

export interface Presentation {
  id: string;
  creator: Creator;
  created_at: string;
  updated_at: string;
  title: string;
  thumbnail: string;
}

export interface PresentationsResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Presentation[];
}
