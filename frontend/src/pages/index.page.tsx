import { Box, Button, Heading, HStack, Input, Select, SimpleGrid, Spinner, VStack } from "@chakra-ui/react";
import React, { useState } from "react";

import { Presentation } from "@/types/presentations";

import PresentationCard from "../components/PresentationCard";
import usePresentations from "../hooks/usePresentations";

export default function Home() {
  const [search, setSearch] = useState<string>("");
  const [ordering, setOrdering] = useState<string>("created_at");
  const [pageUrl, setPageUrl] = useState<string | null>(null);

  const { presentations, error, isValidating, nextPage, prevPage } = usePresentations(search, ordering, pageUrl);

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearch(e.target.value);
    setPageUrl(null);
  };

  const handleOrderingChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setOrdering(e.target.value);
    setPageUrl(null);
  };

  if (error)
    return (
      <VStack my="12">
        <Heading size="lg" as="h1" color="teal.400">
          Opps! Something went wrong
        </Heading>
      </VStack>
    );

  return (
    <Box p={6}>
      <VStack my="12">
        <Heading size="lg" as="h1" color="teal.400">
          Prezi Presentations
        </Heading>
      </VStack>

      <HStack mb={6} spacing={4}>
        <Input placeholder="Search by title..." value={search} onChange={handleSearchChange} />

        <Select value={ordering} onChange={handleOrderingChange}>
          <option value="created_at">Created At Ascending</option>
          <option value="-created_at">Created At Descending</option>
        </Select>
      </HStack>

      {isValidating ? (
        <VStack my="12">
          <Spinner size="lg" color="teal.400" />
        </VStack>
      ) : (
        <SimpleGrid columns={{ sm: 1, md: 2, lg: 3 }} spacing={6}>
          {presentations.map((presentation: Presentation) => (
            <PresentationCard key={presentation.id} presentation={presentation} />
          ))}
        </SimpleGrid>
      )}

      <HStack mt={8} spacing={4} justifyContent="center">
        <Button onClick={() => prevPage && setPageUrl(prevPage)} isDisabled={!prevPage}>
          Previous
        </Button>
        <Button onClick={() => nextPage && setPageUrl(nextPage)} isDisabled={!nextPage}>
          Next
        </Button>
      </HStack>
    </Box>
  );
}
