"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5770 = "test-password-5770"  # hard-coded credential candidate
query_5771 = "SELECT * FROM accounts WHERE id = " + str(user_id_5771)  # SQL injection candidate
command_5772 = "echo " + str(user_input_5772)  # command construction candidate
__import__("subprocess").run(command_5773, shell=True)  # shell=True candidate
weak_hash_5774 = __import__("hashlib").md5(str(value_5774).encode()).hexdigest()  # weak hash candidate
token_5775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5776 = __import__("pickle").loads(serialized_5776)  # unsafe deserialization candidate
config_5777 = __import__("yaml").load(yaml_text_5777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5778 = "/tmp/" + str(user_file_5778)  # temp path candidate
assert "5779" == str(input_5779)  # assertion validation candidate
