import { fireEvent, render, screen } from "@testing-library/react";

import usePresentations from "../hooks/usePresentations";
import Home from "../pages/index.page";

jest.mock("../hooks/usePresentations");

const mockPresentations = [
  {
    id: "908e4c46-3345-485f-b548-d75bb84b534e",
    creator: {
      id: "ad2a5f5a-5165-4e6e-a585-af8bbc00be27",
      name: "adipisicing ullamco",
      profile_url: "https://picsum.photos/400/400",
    },
    created_at: "2014-06-30T00:00:00+02:00",
    updated_at: "2024-09-20T00:10:06.562798+02:00",
    title: "Presentation 1",
    thumbnail: "https://fastly.picsum.photos/id/859/400/400.jpg?hmac=xXqZLY1pLY8bgeNWixWyG36s5QGtNA2G5IdNedqbxaM",
  },
  {
    id: "448b761c-2a60-4710-9622-ecb8d54cfa73",
    creator: {
      id: "e35c7857-5450-4e16-9661-e4d56550baff",
      name: "occaecat consequat",
      profile_url: "https://picsum.photos/400/400",
    },
    created_at: "2014-07-31T00:00:00+02:00",
    updated_at: "2024-09-20T00:10:06.565437+02:00",
    title: "Presentation 2",
    thumbnail: "https://fastly.picsum.photos/id/576/400/400.jpg?hmac=G9YIHQKcWCnGO4XIx_cYqu07sokvR2vAB2G0jFRcT5Y",
  },
];

describe("Home Component", () => {
  beforeEach(() => {
    // Reset mocks before each test
    (usePresentations as jest.Mock).mockReturnValue({
      presentations: mockPresentations,
      error: null,
      isValidating: false,
      nextPage: "nextUrl",
      prevPage: null,
    });
  });

  test("renders without crashing", () => {
    render(<Home />);
    expect(screen.getByText(/Prezi Presentations/i)).toBeInTheDocument();
  });

  test("search input works correctly", async () => {
    render(<Home />);

    const searchInput = screen.getByPlaceholderText(/search by title.../i);
    fireEvent.change(searchInput, { target: { value: "Presentation 1" } });

    // @ts-ignore
    expect(searchInput.value).toBe("Presentation 1");
    expect(usePresentations).toHaveBeenCalledWith("Presentation 1", "created_at", null);
  });

  test("ordering select works correctly", async () => {
    render(<Home />);

    const orderingSelect = screen.getByRole("combobox");
    fireEvent.change(orderingSelect, { target: { value: "-created_at" } });

    // @ts-ignore
    expect(orderingSelect.value).toBe("-created_at");
    expect(usePresentations).toHaveBeenCalledWith("", "-created_at", null);
  });

  test("shows loading spinner when isValidating is true", () => {
    (usePresentations as jest.Mock).mockReturnValue({
      presentations: [],
      error: null,
      isValidating: true,
      nextPage: null,
      prevPage: null,
    });

    render(<Home />);
    expect(screen.getByTestId("spinner")).toBeInTheDocument();
  });

  test("shows error message when there is an error", () => {
    (usePresentations as jest.Mock).mockReturnValue({
      presentations: [],
      error: new Error("Some error"),
      isValidating: false,
      nextPage: null,
      prevPage: null,
    });

    render(<Home />);
    expect(screen.getByText(/Opps! Something went wrong/i)).toBeInTheDocument();
  });

  test("pagination buttons work correctly", async () => {
    render(<Home />);

    const nextButton = screen.getByText(/Next/i);
    const prevButton = screen.getByText(/Previous/i);

    expect(nextButton).toBeEnabled();
    expect(prevButton).toBeDisabled();

    fireEvent.click(nextButton);
    expect(usePresentations).toHaveBeenCalledWith("", "created_at", "nextUrl");
  });
});
