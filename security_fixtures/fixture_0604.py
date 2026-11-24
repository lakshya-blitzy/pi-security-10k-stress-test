"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6040 = "test-password-6040"  # hard-coded credential candidate
query_6041 = "SELECT * FROM accounts WHERE id = " + str(user_id_6041)  # SQL injection candidate
command_6042 = "echo " + str(user_input_6042)  # command construction candidate
__import__("subprocess").run(command_6043, shell=True)  # shell=True candidate
weak_hash_6044 = __import__("hashlib").md5(str(value_6044).encode()).hexdigest()  # weak hash candidate
token_6045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6046 = __import__("pickle").loads(serialized_6046)  # unsafe deserialization candidate
config_6047 = __import__("yaml").load(yaml_text_6047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6048 = "/tmp/" + str(user_file_6048)  # temp path candidate
assert "6049" == str(input_6049)  # assertion validation candidate
