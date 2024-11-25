import React, { useState } from 'react'
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./components/ui/accordion"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "./components/ui/card"
import { Badge } from "./components/ui/badge"

type Response = {
  Ideal: string
  Good: string
  Bad: string
}

type Evidence = {
  Description: string
  Importance: string
  Sufficiency: string
}

type FollowUpAnalysis = {
  Documents_or_Evidence: Record<string, Evidence>
  Open_Source_Tools: string[]
  Commercial_Tools: string[]
}

type AssessmentItem = {
  Question: string
  Responses: Response
  "Follow-up Question": string
  "Follow-up Analysis": FollowUpAnalysis
}

const mockData: AssessmentItem[] = [
  {
    Question: "Does the organization ensure secure interoperability between API components?",
    Responses: {
      Ideal: "Yes, our organization rigorously ensures secure interoperability between components using well-documented and regularly updated APIs. We implement industry-standard authentication, authorization, and encryption protocols, and regularly audit API security and compliance. API security guidelines are adhered to, and development teams are trained in secure coding practices.",
      Good: "Yes, the organization ensures interoperability through APIs but might not yet fully adhere to the latest standards or lacks systematic security audits. APIs are generally secure, and basic security measures like authentication and encryption are in place, but periodic reviews and updates are inconsistent.",
      Bad: "No, the organization does not effectively ensure secure interoperability between API components. Either APIs are not secured as per industry standards, or there is no clear documentation and auditing process to verify the security measures applied."
    },
    "Follow-up Question": "What evidences should be provided to make the answer ideal?",
    "Follow-up Analysis": {
      Documents_or_Evidence: {
        API_Security_Policy: {
          Description: "A documented set of guidelines and standards for secure API development and maintenance.",
          Importance: "High",
          Sufficiency: "Ideal if it is comprehensive and aligns with industry standards like OWASP API Security Top 10."
        },
        Audit_Reports: {
          Description: "Third-party or internal audit reports identifying security assessments and remediation actions.",
          Importance: "High",
          Sufficiency: "Ideal when recent (within the last year), showing resolutions of identified issues."
        }
      },
      Open_Source_Tools: ["OWASP ZAP", "Postman"],
      Commercial_Tools: ["Burp Suite", "Apigee"]
    }
  }
  // Add more assessment items here...
]

export default function Component() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Cybersecurity Assessment</h1>
      <Accordion type="single" collapsible className="w-full">
        {mockData.map((item, index) => (
          <AccordionItem value={`item-${index}`} key={index}>
            <AccordionTrigger>{item.Question}</AccordionTrigger>
            <AccordionContent>
              <Card className="mb-4">
                <CardHeader>
                  <CardTitle>Responses</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-2">
                    <p><Badge variant="outline">Ideal</Badge> {item.Responses.Ideal}</p>
                    <p><Badge variant="outline">Good</Badge> {item.Responses.Good}</p>
                    <p><Badge variant="outline">Bad</Badge> {item.Responses.Bad}</p>
                  </div>
                </CardContent>
              </Card>
              <Card className="mb-4">
                <CardHeader>
                  <CardTitle>Follow-up Question</CardTitle>
                </CardHeader>
                <CardContent>
                  <p>{item["Follow-up Question"]}</p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader>
                  <CardTitle>Follow-up Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  <h3 className="font-semibold mb-2">Required Evidence:</h3>
                  {Object.entries(item["Follow-up Analysis"].Documents_or_Evidence).map(([key, value], i) => (
                    <div key={i} className="mb-2">
                      <h4 className="font-medium">{key}</h4>
                      <p>Description: {value.Description}</p>
                      <p>Importance: {value.Importance}</p>
                      <p>Sufficiency: {value.Sufficiency}</p>
                    </div>
                  ))}
                  <h3 className="font-semibold mt-4 mb-2">Open Source Tools:</h3>
                  <ul className="list-disc pl-5">
                    {item["Follow-up Analysis"].Open_Source_Tools.map((tool, i) => (
                      <li key={i}>{tool}</li>
                    ))}
                  </ul>
                  <h3 className="font-semibold mt-4 mb-2">Commercial Tools:</h3>
                  <ul className="list-disc pl-5">
                    {item["Follow-up Analysis"].Commercial_Tools.map((tool, i) => (
                      <li key={i}>{tool}</li>
                    ))}
                  </ul>
                </CardContent>
              </Card>
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </div>
  )
}