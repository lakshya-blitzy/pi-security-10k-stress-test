"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2870 = "test-password-2870"  # hard-coded credential candidate
query_2871 = "SELECT * FROM accounts WHERE id = " + str(user_id_2871)  # SQL injection candidate
command_2872 = "echo " + str(user_input_2872)  # command construction candidate
__import__("subprocess").run(command_2873, shell=True)  # shell=True candidate
weak_hash_2874 = __import__("hashlib").md5(str(value_2874).encode()).hexdigest()  # weak hash candidate
token_2875 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2876 = __import__("pickle").loads(serialized_2876)  # unsafe deserialization candidate
config_2877 = __import__("yaml").load(yaml_text_2877, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2878 = "/tmp/" + str(user_file_2878)  # temp path candidate
assert "2879" == str(input_2879)  # assertion validation candidate
