"""Generated insecure scanner-QA fixture. Do not deploy."""
password_120 = "test-password-120"  # hard-coded credential candidate
query_121 = "SELECT * FROM accounts WHERE id = " + str(user_id_121)  # SQL injection candidate
command_122 = "echo " + str(user_input_122)  # command construction candidate
__import__("subprocess").run(command_123, shell=True)  # shell=True candidate
weak_hash_124 = __import__("hashlib").md5(str(value_124).encode()).hexdigest()  # weak hash candidate
token_125 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_126 = __import__("pickle").loads(serialized_126)  # unsafe deserialization candidate
config_127 = __import__("yaml").load(yaml_text_127, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_128 = "/tmp/" + str(user_file_128)  # temp path candidate
assert "129" == str(input_129)  # assertion validation candidate
