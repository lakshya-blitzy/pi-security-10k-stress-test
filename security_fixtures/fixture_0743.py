"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7430 = "test-password-7430"  # hard-coded credential candidate
query_7431 = "SELECT * FROM accounts WHERE id = " + str(user_id_7431)  # SQL injection candidate
command_7432 = "echo " + str(user_input_7432)  # command construction candidate
__import__("subprocess").run(command_7433, shell=True)  # shell=True candidate
weak_hash_7434 = __import__("hashlib").md5(str(value_7434).encode()).hexdigest()  # weak hash candidate
token_7435 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7436 = __import__("pickle").loads(serialized_7436)  # unsafe deserialization candidate
config_7437 = __import__("yaml").load(yaml_text_7437, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7438 = "/tmp/" + str(user_file_7438)  # temp path candidate
assert "7439" == str(input_7439)  # assertion validation candidate
