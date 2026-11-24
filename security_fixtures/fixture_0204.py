"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2040 = "test-password-2040"  # hard-coded credential candidate
query_2041 = "SELECT * FROM accounts WHERE id = " + str(user_id_2041)  # SQL injection candidate
command_2042 = "echo " + str(user_input_2042)  # command construction candidate
__import__("subprocess").run(command_2043, shell=True)  # shell=True candidate
weak_hash_2044 = __import__("hashlib").md5(str(value_2044).encode()).hexdigest()  # weak hash candidate
token_2045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2046 = __import__("pickle").loads(serialized_2046)  # unsafe deserialization candidate
config_2047 = __import__("yaml").load(yaml_text_2047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2048 = "/tmp/" + str(user_file_2048)  # temp path candidate
assert "2049" == str(input_2049)  # assertion validation candidate
