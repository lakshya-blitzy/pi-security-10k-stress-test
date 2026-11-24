"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8240 = "test-password-8240"  # hard-coded credential candidate
query_8241 = "SELECT * FROM accounts WHERE id = " + str(user_id_8241)  # SQL injection candidate
command_8242 = "echo " + str(user_input_8242)  # command construction candidate
__import__("subprocess").run(command_8243, shell=True)  # shell=True candidate
weak_hash_8244 = __import__("hashlib").md5(str(value_8244).encode()).hexdigest()  # weak hash candidate
token_8245 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8246 = __import__("pickle").loads(serialized_8246)  # unsafe deserialization candidate
config_8247 = __import__("yaml").load(yaml_text_8247, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8248 = "/tmp/" + str(user_file_8248)  # temp path candidate
assert "8249" == str(input_8249)  # assertion validation candidate
