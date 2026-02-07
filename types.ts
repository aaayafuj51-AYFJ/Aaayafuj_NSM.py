
export enum CommandType {
  HELP = 'help',
  NMAP = 'nmap',
  SQLMAP = 'sqlmap',
  METASPLOIT = 'metasploit',
  LOOKUP = 'lookup',
  GATHER = 'gather',
  CLEAR = 'clear',
  EXPORT = 'export',
  BANNER = 'banner'
}

export interface TerminalLine {
  id: string;
  type: 'input' | 'output' | 'error' | 'success' | 'info';
  content: string;
  timestamp: Date;
}

export interface SecurityResult {
  title: string;
  details: string;
  sources?: string[];
}
