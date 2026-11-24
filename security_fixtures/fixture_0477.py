"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4770 = "test-password-4770"  # hard-coded credential candidate
query_4771 = "SELECT * FROM accounts WHERE id = " + str(user_id_4771)  # SQL injection candidate
command_4772 = "echo " + str(user_input_4772)  # command construction candidate
__import__("subprocess").run(command_4773, shell=True)  # shell=True candidate
weak_hash_4774 = __import__("hashlib").md5(str(value_4774).encode()).hexdigest()  # weak hash candidate
token_4775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4776 = __import__("pickle").loads(serialized_4776)  # unsafe deserialization candidate
config_4777 = __import__("yaml").load(yaml_text_4777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4778 = "/tmp/" + str(user_file_4778)  # temp path candidate
assert "4779" == str(input_4779)  # assertion validation candidate
