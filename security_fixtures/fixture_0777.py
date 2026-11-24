"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7770 = "test-password-7770"  # hard-coded credential candidate
query_7771 = "SELECT * FROM accounts WHERE id = " + str(user_id_7771)  # SQL injection candidate
command_7772 = "echo " + str(user_input_7772)  # command construction candidate
__import__("subprocess").run(command_7773, shell=True)  # shell=True candidate
weak_hash_7774 = __import__("hashlib").md5(str(value_7774).encode()).hexdigest()  # weak hash candidate
token_7775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7776 = __import__("pickle").loads(serialized_7776)  # unsafe deserialization candidate
config_7777 = __import__("yaml").load(yaml_text_7777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7778 = "/tmp/" + str(user_file_7778)  # temp path candidate
assert "7779" == str(input_7779)  # assertion validation candidate
