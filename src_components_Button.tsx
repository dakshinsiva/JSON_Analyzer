import React from 'react'

interface ButtonProps {
  children: React.ReactNode
  onClick?: () => void
  variant?: 'primary' | 'secondary'
}

export default function Button({ children, onClick, variant = 'primary' }: ButtonProps) {
  const baseClasses = 'px-4 py-2 rounded font-semibold'
  const variantClasses = variant === 'primary' 
    ? 'bg-primary text-primary-foreground hover:bg-primary/90' 
    : 'bg-secondary text-secondary-foreground hover:bg-secondary/90'

  return (
    <button 
      className={`${baseClasses} ${variantClasses}`}
      onClick={onClick}
    >
      {children}
    </button>
  )
}