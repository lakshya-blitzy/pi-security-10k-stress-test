"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3060 = "test-password-3060"  # hard-coded credential candidate
query_3061 = "SELECT * FROM accounts WHERE id = " + str(user_id_3061)  # SQL injection candidate
command_3062 = "echo " + str(user_input_3062)  # command construction candidate
__import__("subprocess").run(command_3063, shell=True)  # shell=True candidate
weak_hash_3064 = __import__("hashlib").md5(str(value_3064).encode()).hexdigest()  # weak hash candidate
token_3065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3066 = __import__("pickle").loads(serialized_3066)  # unsafe deserialization candidate
config_3067 = __import__("yaml").load(yaml_text_3067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3068 = "/tmp/" + str(user_file_3068)  # temp path candidate
assert "3069" == str(input_3069)  # assertion validation candidate
