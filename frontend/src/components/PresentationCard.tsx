import { Box, Heading, Image, Text, VStack } from "@chakra-ui/react";

import { Presentation } from "@/types/presentations";

interface PresentationCardProps {
  presentation: Presentation;
}

const PresentationCard = ({ presentation }: PresentationCardProps) => {
  return (
    <Box border="1px" borderColor="gray.200" borderRadius="md" p={4} shadow="sm" display="flex" alignItems="center">
      <Image src={presentation.thumbnail} alt={presentation.title} boxSize="150px" objectFit="cover" mr={4} />
      <VStack align="start">
        <Heading size="md">{presentation.title}</Heading>
        <Text>By: {presentation.creator.name}</Text>
        <Text>Created At: {new Date(presentation.created_at).toLocaleDateString()}</Text>
      </VStack>
    </Box>
  );
};

export default PresentationCard;
