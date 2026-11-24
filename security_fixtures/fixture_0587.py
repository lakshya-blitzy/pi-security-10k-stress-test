"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5870 = "test-password-5870"  # hard-coded credential candidate
query_5871 = "SELECT * FROM accounts WHERE id = " + str(user_id_5871)  # SQL injection candidate
command_5872 = "echo " + str(user_input_5872)  # command construction candidate
__import__("subprocess").run(command_5873, shell=True)  # shell=True candidate
weak_hash_5874 = __import__("hashlib").md5(str(value_5874).encode()).hexdigest()  # weak hash candidate
token_5875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5876 = __import__("pickle").loads(serialized_5876)  # unsafe deserialization candidate
config_5877 = __import__("yaml").load(yaml_text_5877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5878 = "/tmp/" + str(user_file_5878)  # temp path candidate
assert "5879" == str(input_5879)  # assertion validation candidate
