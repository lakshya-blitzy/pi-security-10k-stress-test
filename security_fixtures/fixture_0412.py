"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4120 = "test-password-4120"  # hard-coded credential candidate
query_4121 = "SELECT * FROM accounts WHERE id = " + str(user_id_4121)  # SQL injection candidate
command_4122 = "echo " + str(user_input_4122)  # command construction candidate
__import__("subprocess").run(command_4123, shell=True)  # shell=True candidate
weak_hash_4124 = __import__("hashlib").md5(str(value_4124).encode()).hexdigest()  # weak hash candidate
token_4125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4126 = __import__("pickle").loads(serialized_4126)  # unsafe deserialization candidate
config_4127 = __import__("yaml").load(yaml_text_4127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4128 = "/tmp/" + str(user_file_4128)  # temp path candidate
assert "4129" == str(input_4129)  # assertion validation candidate
