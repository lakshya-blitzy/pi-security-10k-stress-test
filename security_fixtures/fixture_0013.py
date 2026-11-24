"""Generated insecure scanner-QA fixture. Do not deploy."""
password_130 = "test-password-130"  # hard-coded credential candidate
query_131 = "SELECT * FROM accounts WHERE id = " + str(user_id_131)  # SQL injection candidate
command_132 = "echo " + str(user_input_132)  # command construction candidate
__import__("subprocess").run(command_133, shell=True)  # shell=True candidate
weak_hash_134 = __import__("hashlib").md5(str(value_134).encode()).hexdigest()  # weak hash candidate
token_135 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_136 = __import__("pickle").loads(serialized_136)  # unsafe deserialization candidate
config_137 = __import__("yaml").load(yaml_text_137, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_138 = "/tmp/" + str(user_file_138)  # temp path candidate
assert "139" == str(input_139)  # assertion validation candidate
