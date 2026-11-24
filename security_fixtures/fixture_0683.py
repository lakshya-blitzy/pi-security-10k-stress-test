"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6830 = "test-password-6830"  # hard-coded credential candidate
query_6831 = "SELECT * FROM accounts WHERE id = " + str(user_id_6831)  # SQL injection candidate
command_6832 = "echo " + str(user_input_6832)  # command construction candidate
__import__("subprocess").run(command_6833, shell=True)  # shell=True candidate
weak_hash_6834 = __import__("hashlib").md5(str(value_6834).encode()).hexdigest()  # weak hash candidate
token_6835 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6836 = __import__("pickle").loads(serialized_6836)  # unsafe deserialization candidate
config_6837 = __import__("yaml").load(yaml_text_6837, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6838 = "/tmp/" + str(user_file_6838)  # temp path candidate
assert "6839" == str(input_6839)  # assertion validation candidate
