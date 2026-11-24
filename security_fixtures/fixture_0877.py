"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8770 = "test-password-8770"  # hard-coded credential candidate
query_8771 = "SELECT * FROM accounts WHERE id = " + str(user_id_8771)  # SQL injection candidate
command_8772 = "echo " + str(user_input_8772)  # command construction candidate
__import__("subprocess").run(command_8773, shell=True)  # shell=True candidate
weak_hash_8774 = __import__("hashlib").md5(str(value_8774).encode()).hexdigest()  # weak hash candidate
token_8775 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8776 = __import__("pickle").loads(serialized_8776)  # unsafe deserialization candidate
config_8777 = __import__("yaml").load(yaml_text_8777, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8778 = "/tmp/" + str(user_file_8778)  # temp path candidate
assert "8779" == str(input_8779)  # assertion validation candidate
