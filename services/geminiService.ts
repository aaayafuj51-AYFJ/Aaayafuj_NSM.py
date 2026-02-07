
import { GoogleGenAI, GenerateContentResponse } from "@google/genai";

const getAI = () => new GoogleGenAI({ apiKey: process.env.API_KEY });

export async function analyzeSecurityTask(module: string, target: string): Promise<{ text: string; sources?: string[] }> {
  const ai = getAI();
  const model = 'gemini-3-pro-preview';

  let prompt = "";
  let useSearch = false;

  switch (module) {
    case 'nmap':
      prompt = `Act as an Nmap expert. Provide a simulated technical analysis for target "${target}". 
      Include potential open ports for this type of target, typical services (SSH, HTTP, etc.), 
      and security recommendations. Format as a terminal output with brackets and timestamps.`;
      break;
    case 'sqlmap':
      prompt = `Analyze the URL "${target}" for potential SQL injection vulnerabilities. 
      Explain common parameters to test and what types of SQLi might be applicable (Boolean-based, Time-based, etc.). 
      Do NOT perform illegal actions. Educational analysis only.`;
      break;
    case 'metasploit':
      prompt = `Search for Metasploit modules related to "${target}". List relevant exploit modules, 
      payloads, and auxiliary scanners. Provide the module paths (e.g., exploit/windows/smb/ms17_010_eternalblue).`;
      break;
    case 'lookup':
      prompt = `Perform a comprehensive DNS and WHOIS lookup for "${target}". 
      Provide registrar information, name servers, and IP resolution history if possible. Use search for accuracy.`;
      useSearch = true;
      break;
    case 'gather':
      prompt = `Gather detailed OSINT (Open Source Intelligence) for target "${target}". 
      Include hosting provider, server technology, possible subdomains, and historical data. Use search for current data.`;
      useSearch = true;
      break;
    default:
      prompt = `Analyze target "${target}" in the context of network security.`;
  }

  const response: GenerateContentResponse = await ai.models.generateContent({
    model,
    contents: prompt,
    config: {
      tools: useSearch ? [{ googleSearch: {} }] : undefined,
    },
  });

  const text = response.text || "No output generated.";
  const sources = response.candidates?.[0]?.groundingMetadata?.groundingChunks
    ?.map((chunk: any) => chunk.web?.uri)
    .filter((uri: string) => !!uri);

  return { text, sources };
}
