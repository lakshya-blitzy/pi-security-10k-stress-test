"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6720 = "test-password-6720"  # hard-coded credential candidate
query_6721 = "SELECT * FROM accounts WHERE id = " + str(user_id_6721)  # SQL injection candidate
command_6722 = "echo " + str(user_input_6722)  # command construction candidate
__import__("subprocess").run(command_6723, shell=True)  # shell=True candidate
weak_hash_6724 = __import__("hashlib").md5(str(value_6724).encode()).hexdigest()  # weak hash candidate
token_6725 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6726 = __import__("pickle").loads(serialized_6726)  # unsafe deserialization candidate
config_6727 = __import__("yaml").load(yaml_text_6727, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6728 = "/tmp/" + str(user_file_6728)  # temp path candidate
assert "6729" == str(input_6729)  # assertion validation candidate
