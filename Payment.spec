
# Payment Overlay

## Check the Payment overlay during Checkout

* The user proceed to the make the payment
* The payment block is composed of 
	- The title "Billing Information" (editable)
	- The back arrow to return to the shipping address page
	- Billing address section, that displays the selected billing address
	- Email text field
	- Payment section - text field to enter CC details
	- CTA to SUBMIT 
	- The shipping address details & the option to "Change" it


## Payment Scenario - Proceed to make payment keeping Billing Address should be same as shipping Address

* The user proceed to the make the payment
* A text saying "Same as shipping address" should be visible
* The checkbox is by default selected
* The user enters the email address (Mandatory field)
* The user enters the information for the payment card (Card Number | expiry | CVV)
* User clicks on the CTA to Pay
* User should be directed to the order confirmation page


## Payment Scenario - Proceed to make payment after unchecking the "Same as shipping address" checkbox

* The user proceed to the make the payment
* A text saying "Same as shipping address" should be visible
* The checkbox is by default selected
* The user un-selects the checkbox for "Same as shipping address"
	- The text box to search a billing address should appear
	- The CTA to "Enter address manually" should appear
	- Click on the "Enter address manually" should open the form to enter the billing address - user should be able to enter the billing address
* The user enters the email address (Mandatory field)
* The user enters the information for the payment card (Card Number | expiry | CVV)
* User clicks on the CTA to Pay
* User should be directed to the order confirmation page


## Verifying the "Shipping Address" section on the payment overlay

* The user proceed to the make the payment
* User should see the block below the PAY CTA 
* The shipping address should eb the one enterred by the user
* User should be able to click on the "Change" CTA 
* Click on "Change" CTA should re-direct the user to the shipping address page
* The user should be able to change the Shipping address and proceed back to the payment page
* The edited shipping address should now be visible on the payment page
