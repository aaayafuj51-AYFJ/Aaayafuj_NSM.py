
import React from 'react';
import { TerminalLine } from '../types';

interface TerminalOutputProps {
  lines: TerminalLine[];
}

const TerminalOutput: React.FC<TerminalOutputProps> = ({ lines }) => {
  return (
    <div className="flex flex-col gap-1">
      {lines.map((line) => (
        <div key={line.id} className="whitespace-pre-wrap break-all">
          {line.type === 'input' && (
            <div className="flex gap-2">
              <span className="text-blue-400">root@aaayafuj</span>
              <span className="text-white">:</span>
              <span className="text-purple-400">~</span>
              <span className="text-white">$</span>
              <span>{line.content}</span>
            </div>
          )}
          {line.type === 'output' && (
            <div className="text-green-400 opacity-90">{line.content}</div>
          )}
          {line.type === 'info' && (
            <div className="text-cyan-400 italic">[*] {line.content}</div>
          )}
          {line.type === 'error' && (
            <div className="text-red-500 font-bold">[!] {line.content}</div>
          )}
          {line.type === 'success' && (
            <div className="text-green-500 font-bold">[+] {line.content}</div>
          )}
        </div>
      ))}
    </div>
  );
};

export default TerminalOutput;
