import { extendTheme, withDefaultColorScheme } from "@chakra-ui/react";

export const theme = extendTheme(withDefaultColorScheme({ colorScheme: "teal" }), {
  styles: {
    global: () => ({
      body: { bg: "gray.50" },
    }),
  },
  sizes: {
    container: {
      "2xl": "1440px",
    },
  },
});
