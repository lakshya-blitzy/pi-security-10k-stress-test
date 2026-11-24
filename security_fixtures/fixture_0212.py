"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2120 = "test-password-2120"  # hard-coded credential candidate
query_2121 = "SELECT * FROM accounts WHERE id = " + str(user_id_2121)  # SQL injection candidate
command_2122 = "echo " + str(user_input_2122)  # command construction candidate
__import__("subprocess").run(command_2123, shell=True)  # shell=True candidate
weak_hash_2124 = __import__("hashlib").md5(str(value_2124).encode()).hexdigest()  # weak hash candidate
token_2125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2126 = __import__("pickle").loads(serialized_2126)  # unsafe deserialization candidate
config_2127 = __import__("yaml").load(yaml_text_2127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2128 = "/tmp/" + str(user_file_2128)  # temp path candidate
assert "2129" == str(input_2129)  # assertion validation candidate
