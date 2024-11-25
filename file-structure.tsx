import React from 'react'
import { FolderTree, Folder, File } from 'lucide-react'

export default function Component() {
  return (
    <div className="p-4 bg-background text-foreground">
      <h2 className="text-2xl font-bold mb-4">React Project File Structure</h2>
      <div className="font-mono text-sm">
        <FolderTree>
          <Folder name="src">
            <Folder name="components">
              <File name="Button.tsx" />
              <File name="Card.tsx" />
              <File name="Header.tsx" />
              <File name="Footer.tsx" />
            </Folder>
            <Folder name="layouts">
              <File name="MainLayout.tsx" />
            </Folder>
            <Folder name="pages">
              <File name="Home.tsx" />
              <File name="About.tsx" />
              <File name="Contact.tsx" />
            </Folder>
            <Folder name="styles">
              <File name="globals.css" />
            </Folder>
            <Folder name="utils">
              <File name="api.ts" />
              <File name="helpers.ts" />
            </Folder>
            <File name="App.tsx" />
            <File name="index.tsx" />
          </Folder>
          <File name="package.json" />
          <File name="tsconfig.json" />
          <File name="README.md" />
        </FolderTree>
      </div>
    </div>
  )
}