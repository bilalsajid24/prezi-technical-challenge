import { ChakraProvider } from "@chakra-ui/react";
import { NextPage } from "next";
import { AppProps } from "next/app";

import { theme } from "@/theme";

export interface PresentationAppProps extends AppProps {
  Component: NextPage;
}

function PresentationApp(props: PresentationAppProps) {
  const { Component, pageProps } = props;

  return (
    <ChakraProvider theme={theme} resetCSS>
      <Component {...pageProps} />
    </ChakraProvider>
  );
}

export default PresentationApp;
