"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6770 = "test-password-6770"  # hard-coded credential candidate
query_6771 = "SELECT * FROM accounts WHERE id = " + str(user_id_6771)  # SQL injection candidate
command_6772 = "echo " + str(user_input_6772)  # command construction candidate
__import__("subprocess").run(command_6773, shell=True)  # shell=True candidate
weak_hash_6774 = __import__("hashlib").md5(str(value_6774).encode()).hexdigest()  # weak hash candidate
token_6775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6776 = __import__("pickle").loads(serialized_6776)  # unsafe deserialization candidate
config_6777 = __import__("yaml").load(yaml_text_6777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6778 = "/tmp/" + str(user_file_6778)  # temp path candidate
assert "6779" == str(input_6779)  # assertion validation candidate
