import "@testing-library/jest-dom";

import { ReactElement } from "react";
// eslint-disable-next-line global-require
jest.mock("next/router", () => require("next-router-mock"));
jest.mock("@amplitude/analytics-browser");
jest.mock("@/client", () => ({
  client: { request: jest.fn() },
}));

// https://github.com/vercel/next.js/discussions/11060#discussioncomment-33628
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
