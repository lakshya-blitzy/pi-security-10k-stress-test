"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3120 = "test-password-3120"  # hard-coded credential candidate
query_3121 = "SELECT * FROM accounts WHERE id = " + str(user_id_3121)  # SQL injection candidate
command_3122 = "echo " + str(user_input_3122)  # command construction candidate
__import__("subprocess").run(command_3123, shell=True)  # shell=True candidate
weak_hash_3124 = __import__("hashlib").md5(str(value_3124).encode()).hexdigest()  # weak hash candidate
token_3125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3126 = __import__("pickle").loads(serialized_3126)  # unsafe deserialization candidate
config_3127 = __import__("yaml").load(yaml_text_3127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3128 = "/tmp/" + str(user_file_3128)  # temp path candidate
assert "3129" == str(input_3129)  # assertion validation candidate
