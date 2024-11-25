// First, let's define our standardized types
type Response = {
    ideal: string;
    good: string;
    bad: string;
  }
  
  type Evidence = {
    document: string;
    importance: string;
    sufficiency: string;
    openSourceTools?: string[];
    commercialTools?: string[];
  }
  
  type AssessmentItem = {
    id: string;
    question: string;
    responses: Response;
    followUpQuestion: string;
    evidence: Evidence[];
  }