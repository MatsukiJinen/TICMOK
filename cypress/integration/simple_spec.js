describe('My First Test', function() {
  it('Does not do much!', function() {
    expect(true).to.equal(true)
  })
})

describe('My First Test', function() {
  it('call to action01', function() {
    cy.viewport('macbook-13')
      cy.visit(`https://mockup-generetor.dev/all/call_to_action/01.html`)
      cy.screenshot()
  })
})

describe('My First Test', function() {
  it('call to action02', function() {
    cy.viewport('macbook-13')
      cy.visit(`https://mockup-generetor.dev/all/call_to_action/02.html`)
      cy.screenshot()
  })
})
