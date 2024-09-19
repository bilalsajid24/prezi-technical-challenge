import { Heading, Text, VStack } from "@chakra-ui/react";
import type { NextPage } from "next";

const Home: NextPage = () => {
  return (
    <VStack my="12">
      <Heading size="lg" as="h1" color="teal.400">
        Presentations
      </Heading>
      <Text size="2xl" as="h2" color="secondary">
        Presentations for Prezi
      </Text>
    </VStack>
  );
};

export default Home;
