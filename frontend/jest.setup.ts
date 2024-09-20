import "@testing-library/jest-dom";

import { ReactElement } from "react";

jest.mock("next/head", () => {
  return {
    __esModule: true,
    default: ({ children }: { children: Array<ReactElement> }) => {
      return children;
    },
  };
});

afterEach(() => {
  jest.resetAllMocks();
});
