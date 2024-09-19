import Document, { DocumentProps, Head, Html, Main, NextScript } from "next/document";

import { theme } from "@/theme";

interface BazarDocumentProps extends DocumentProps {
  emotionStyleTags: JSX.Element[];
}

export default class BazarDocument extends Document<BazarDocumentProps> {
  render() {
    return (
      <Html lang="en">
        <Head>
          <meta name="theme-color" content={theme.colors.teal["400"]} />
          <link rel="shortcut icon" href="/static/favicon.ico" />
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}
